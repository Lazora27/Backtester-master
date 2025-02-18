import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
