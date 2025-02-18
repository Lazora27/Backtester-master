import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
