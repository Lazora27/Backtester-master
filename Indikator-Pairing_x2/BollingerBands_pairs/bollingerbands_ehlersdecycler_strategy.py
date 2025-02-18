import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'EhlersDecycler': 1.0
        })
    )
