import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
