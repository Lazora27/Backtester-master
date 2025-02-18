import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'FlowOfFunds': 1.0
        })
    )
