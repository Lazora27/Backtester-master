import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
