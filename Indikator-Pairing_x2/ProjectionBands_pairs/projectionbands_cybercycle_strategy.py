import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und CyberCycle
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'CyberCycle': 1.0
        })
    )
