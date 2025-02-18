import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und DPOCycles
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'DPOCycles': 1.0
        })
    )
