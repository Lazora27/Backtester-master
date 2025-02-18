import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'DPOCycles': 1.0
        })
    )
