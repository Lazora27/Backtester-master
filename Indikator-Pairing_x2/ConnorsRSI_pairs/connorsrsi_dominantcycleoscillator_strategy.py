import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
