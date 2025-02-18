import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'ProjectionBands': 1.0
        })
    )
