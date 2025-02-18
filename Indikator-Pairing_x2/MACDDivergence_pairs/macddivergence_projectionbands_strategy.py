import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'ProjectionBands': 1.0
        })
    )
