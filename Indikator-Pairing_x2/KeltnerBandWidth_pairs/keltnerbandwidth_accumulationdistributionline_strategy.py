import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
