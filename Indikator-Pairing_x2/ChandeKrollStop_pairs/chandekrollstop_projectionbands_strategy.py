import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'ProjectionBands': 1.0
        })
    )
