import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
