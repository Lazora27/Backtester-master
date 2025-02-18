import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierTransformAnalysis_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierTransformAnalysis und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'FourierTransformAnalysis': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
