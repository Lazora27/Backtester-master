import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
