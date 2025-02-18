import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'ModifiedATR': 1.0
        })
    )
