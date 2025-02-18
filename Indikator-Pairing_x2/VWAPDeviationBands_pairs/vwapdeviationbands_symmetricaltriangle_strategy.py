import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
