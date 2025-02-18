import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'ProjectionBands': 1.0
        })
    )
