import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
