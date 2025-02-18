import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
