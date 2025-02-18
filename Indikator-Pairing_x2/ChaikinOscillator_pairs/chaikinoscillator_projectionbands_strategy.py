import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'ProjectionBands': 1.0
        })
    )
