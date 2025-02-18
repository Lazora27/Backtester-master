import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_ChaikinMoneyFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und ChaikinMoneyFlow
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'ChaikinMoneyFlow': {
                'class': ChaikinMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinMoneyFlow'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'ChaikinMoneyFlow': 1.0
        })
    )
