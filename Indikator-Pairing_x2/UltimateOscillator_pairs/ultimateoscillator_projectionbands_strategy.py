import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'ProjectionBands': 1.0
        })
    )
