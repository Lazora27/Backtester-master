import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'DeltaProfile': 1.0
        })
    )
