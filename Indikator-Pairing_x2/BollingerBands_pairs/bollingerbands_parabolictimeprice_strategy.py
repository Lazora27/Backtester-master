import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
