import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'FlowOfFunds': 1.0
        })
    )
