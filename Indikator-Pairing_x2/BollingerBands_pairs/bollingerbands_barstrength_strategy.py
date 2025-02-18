import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und BarStrength
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'BarStrength': 1.0
        })
    )
