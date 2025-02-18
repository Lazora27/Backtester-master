import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'FlowOfFunds': 1.0
        })
    )
