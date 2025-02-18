import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
