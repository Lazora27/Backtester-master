import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
