import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'FlowOfFunds': 1.0
        })
    )
