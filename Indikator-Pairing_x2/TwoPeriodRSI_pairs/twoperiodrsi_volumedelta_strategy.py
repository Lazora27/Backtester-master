import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'VolumeDelta': 1.0
        })
    )
