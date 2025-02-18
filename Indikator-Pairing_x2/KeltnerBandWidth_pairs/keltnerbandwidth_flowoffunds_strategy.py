import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'FlowOfFunds': 1.0
        })
    )
