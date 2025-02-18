import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
