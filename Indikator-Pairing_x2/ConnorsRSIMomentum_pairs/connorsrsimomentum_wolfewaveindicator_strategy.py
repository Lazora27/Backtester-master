import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSIMomentum_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSIMomentum und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'ConnorsRSIMomentum': {
                'class': ConnorsRSIMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSIMomentum'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'ConnorsRSIMomentum': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
