import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und MassIndex
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'MassIndex': 1.0
        })
    )
