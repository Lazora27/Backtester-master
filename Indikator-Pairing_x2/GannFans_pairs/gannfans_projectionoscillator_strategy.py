import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
