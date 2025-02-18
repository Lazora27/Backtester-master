import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
