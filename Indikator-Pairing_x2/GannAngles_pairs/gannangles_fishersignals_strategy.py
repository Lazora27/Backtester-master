import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und FisherSignals
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'FisherSignals': 1.0
        })
    )
