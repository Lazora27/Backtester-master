import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und TrendCycles
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'TrendCycles': 1.0
        })
    )
