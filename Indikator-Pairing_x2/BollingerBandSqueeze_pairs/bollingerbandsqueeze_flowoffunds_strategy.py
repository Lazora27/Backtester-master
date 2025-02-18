import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'FlowOfFunds': 1.0
        })
    )
