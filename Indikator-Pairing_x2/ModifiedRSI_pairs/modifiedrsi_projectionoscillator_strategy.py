import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
