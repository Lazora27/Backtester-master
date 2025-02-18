import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
