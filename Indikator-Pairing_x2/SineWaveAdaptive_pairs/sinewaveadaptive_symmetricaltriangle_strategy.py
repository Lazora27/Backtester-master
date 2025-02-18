import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SineWaveAdaptive_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SineWaveAdaptive und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'SineWaveAdaptive': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
