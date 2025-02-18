import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
