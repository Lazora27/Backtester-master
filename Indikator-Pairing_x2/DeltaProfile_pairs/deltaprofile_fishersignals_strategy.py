import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und FisherSignals
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'FisherSignals': 1.0
        })
    )
