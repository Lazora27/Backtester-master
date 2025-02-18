import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
