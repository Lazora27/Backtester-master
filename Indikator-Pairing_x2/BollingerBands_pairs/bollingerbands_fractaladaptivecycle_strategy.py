import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_FractalAdaptiveCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und FractalAdaptiveCycle
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'FractalAdaptiveCycle': {
                'class': FractalAdaptiveCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalAdaptiveCycle'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'FractalAdaptiveCycle': 1.0
        })
    )
