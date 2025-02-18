import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'KeltnerChannels': 1.0
        })
    )
