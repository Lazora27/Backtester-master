import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'ProjectionBands': 1.0
        })
    )
