import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'ProjectionBands': 1.0
        })
    )
