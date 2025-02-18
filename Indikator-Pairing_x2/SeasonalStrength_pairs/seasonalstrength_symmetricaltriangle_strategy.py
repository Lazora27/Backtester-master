import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SeasonalStrength_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SeasonalStrength und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'SeasonalStrength': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
