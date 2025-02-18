import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'KeltnerChannels': 1.0
        })
    )
